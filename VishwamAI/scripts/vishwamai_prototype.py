import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import os
from transformers import GPT2Tokenizer, TFGPT2Model
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from scipy.linalg import sqrtm

# Configure TensorFlow for dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

class VishwamAI:
    def __init__(self, batch_size):
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
        self.gan = self.build_gan(self.generator, self.discriminator)
        self.nlp_model, self.tokenizer = self.build_nlp_model()
        self.sample_dataset = self.load_sample_dataset(batch_size)

    def build_generator(self):
        model = models.Sequential()
        model.add(layers.Input(shape=(100,)))
        model.add(layers.Dense(135 * 135 * 16, activation='tanh'))
        model.add(layers.Reshape((135, 135, 16)))
        model.add(layers.Conv2DTranspose(512, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        print(model.output_shape)
        model.add(layers.Conv2DTranspose(256, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        print(model.output_shape)
        model.add(layers.Conv2DTranspose(128, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        print(model.output_shape)
        model.add(layers.Conv2DTranspose(64, (4, 4), strides=(1, 1), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        print(model.output_shape)
        model.add(layers.Conv2DTranspose(32, (4, 4), strides=(1, 1), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        print(model.output_shape)
        model.add(layers.Conv2DTranspose(3, (4, 4), strides=(1, 1), padding='same', activation='tanh'))
        print(model.output_shape)
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model

    def build_discriminator(self):
        model = models.Sequential()
        model.add(layers.Conv2D(32, (4, 4), strides=(2, 2), padding='same', input_shape=(1080, 1080, 3)))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        model.add(layers.Conv2D(64, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        model.add(layers.Conv2D(128, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        model.add(layers.Conv2D(256, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        model.add(layers.Conv2D(512, (4, 4), strides=(2, 2), padding='same'))
        model.add(layers.LeakyReLU(negative_slope=0.2))
        model.add(layers.Flatten())
        model.add(layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def build_gan(self, generator, discriminator):
        discriminator.trainable = False
        gan_input = layers.Input(shape=(100,))
        generated_image = generator(gan_input)
        gan_output = discriminator(generated_image)
        gan = models.Model(gan_input, gan_output)
        gan.compile(optimizer='adam', loss='binary_crossentropy')
        return gan

    def build_nlp_model(self):
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        model = TFGPT2Model.from_pretrained("gpt2")
        dummy_input = tf.constant([[0] * 10])  # Dummy input with shape (1, 10)
        model(dummy_input)  # Build the model with the dummy input
        return model, tokenizer

    def load_sample_dataset(self, batch_size):
        def preprocess_image(image_path):
            image_path = str(image_path)  # Ensure image_path is a string
            image = tf.io.read_file(image_path)
            image = tf.image.decode_jpeg(image, channels=3)
            image = tf.image.resize(image, [1080, 1080])
            image = (image - 127.5) / 127.5  # Normalize to [-1, 1]
            return image

        image_paths = [os.path.join('/home/ubuntu/VishwamAI/data/sample_dataset', image_path)
                       for image_path in os.listdir('/home/ubuntu/VishwamAI/data/sample_dataset')
                       if image_path.lower().endswith(('.jpg', '.jpeg', '.png'))]

        dataset = tf.data.Dataset.from_tensor_slices(image_paths)
        dataset = dataset.map(preprocess_image, num_parallel_calls=tf.data.experimental.AUTOTUNE)
        dataset = dataset.shuffle(buffer_size=len(image_paths))
        dataset = dataset.batch(batch_size)
        dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return dataset

    def train(self, epochs, batch_size):
        # Training loop for GAN
        half_batch = int(batch_size / 2)
        print(f"Batch size: {batch_size}, Half batch: {half_batch}")
        for epoch in range(epochs):
            for real_images in self.sample_dataset:
                # Train Discriminator
                noise = np.random.normal(0, 1, (half_batch, 100))
                generated_images = self.generator.predict(noise)
                d_loss_real = self.discriminator.train_on_batch(real_images[:half_batch], np.ones((half_batch, 1)))
                d_loss_fake = self.discriminator.train_on_batch(generated_images, np.zeros((half_batch, 1)))
                d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

                # Train Generator
                noise = np.random.normal(0, 1, (batch_size, 100))
                valid_y = np.array([1] * batch_size)
                g_loss = self.gan.train_on_batch(noise, valid_y)

                # Print the progress
                print(f"{epoch} [D loss: {d_loss[0]} | D accuracy: {d_loss[1]}] [G loss: {g_loss}]")

                # Save model checkpoints
                if epoch % 1000 == 0:
                    self.generator.save(f'models/generator_epoch_{epoch}.h5')
                    self.discriminator.save(f'models/discriminator_epoch_{epoch}.h5')

    def self_improve(self):
        # Evaluate model performance
        performance_metrics = self.evaluate_performance()

        # Search for new data
        new_data = self.search_new_data()

        # Integrate new data into training process
        self.integrate_new_data(new_data)

        # Update model training
        self.train(epochs=1000, batch_size=32)

    def evaluate_performance(self):
        from tensorflow.keras.applications.inception_v3 import InceptionV3
        from tensorflow.keras.applications.inception_v3 import preprocess_input
        from scipy.linalg import sqrtm
        import numpy as np

        # Load the InceptionV3 model for calculating IS and FID
        model = InceptionV3(include_top=False, pooling='avg', input_shape=(299, 299, 3))

        # Generate a batch of images
        noise = np.random.normal(0, 1, (100, 100))
        generated_images = self.generator.predict(noise)

        # Preprocess the images for InceptionV3
        generated_images = tf.image.resize(generated_images, (299, 299))
        generated_images = preprocess_input(generated_images)

        # Calculate the activations for the generated images
        act_gen = model.predict(generated_images)

        # Calculate the mean and covariance of the activations
        mu_gen = np.mean(act_gen, axis=0)
        sigma_gen = np.cov(act_gen, rowvar=False)

        # Load a batch of real images
        idx = np.random.randint(0, self.sample_dataset.shape[0], 100)
        real_images = self.sample_dataset[idx]

        # Preprocess the real images for InceptionV3
        real_images = tf.image.resize(real_images, (299, 299))
        real_images = preprocess_input(real_images)

        # Calculate the activations for the real images
        act_real = model.predict(real_images)

        # Calculate the mean and covariance of the activations
        mu_real = np.mean(act_real, axis=0)
        sigma_real = np.cov(act_real, rowvar=False)

        # Calculate the Fréchet Inception Distance (FID)
        ssdiff = np.sum((mu_gen - mu_real)**2.0)
        covmean = sqrtm(sigma_gen.dot(sigma_real))
        if np.iscomplexobj(covmean):
            covmean = covmean.real
        fid = ssdiff + np.trace(sigma_gen + sigma_real - 2.0 * covmean)

        # Calculate the Inception Score (IS)
        p_yx = act_gen
        p_y = np.expand_dims(np.mean(p_yx, axis=0), 0)
        kl_d = p_yx * (np.log(p_yx + 1e-10) - np.log(p_y + 1e-10))
        is_score = np.exp(np.mean(np.sum(kl_d, axis=1)))

        return {'FID': fid, 'IS': is_score}

    def search_new_data(self):
        import requests
        from bs4 import BeautifulSoup
        import urllib

        # Define the URL to scrape images from
        url = "https://unsplash.com/s/photos/sample"

        # Send a request to the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all image tags
        img_tags = soup.find_all("img")

        # Create a directory to save the new images
        new_data_dir = "data/new_data"
        if not os.path.exists(new_data_dir):
            os.makedirs(new_data_dir)

        # Download and save the images
        new_data = []
        for img in img_tags:
            img_url = img.get("src")
            if img_url:
                img_data = requests.get(img_url).content
                img_name = os.path.join(new_data_dir, os.path.basename(img_url))
                with open(img_name, "wb") as handler:
                    handler.write(img_data)
                new_data.append(img_name)

        return new_data

    def integrate_new_data(self, new_data):
        # Load and preprocess the new data
        for image_path in new_data:
            if image_path.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(1080, 1080))
                    image = tf.keras.preprocessing.image.img_to_array(image)
                    image = (image - 127.5) / 127.5  # Normalize to [-1, 1]
                    self.sample_dataset = np.append(self.sample_dataset, [image], axis=0)
                except Exception as e:
                    print(f"Error loading image {image_path}: {e}")

def test_data_generator(batch_size=2):
    vishwamai = VishwamAI(batch_size=batch_size)
    dataset = vishwamai.load_sample_dataset(batch_size)
    for i, batch in enumerate(dataset.take(5)):
        print(f"Batch {i+1}: {batch.shape}")
    print("Data generator test completed successfully.")

if __name__ == "__main__":
    test_data_generator(batch_size=2)

def test_generate_images(input_text, num_images=10, output_dir="generated_images"):
    vishwamai = VishwamAI(batch_size=32)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(num_images):
        generated_image = vishwamai.generate_image(input_text)
        generated_image = (generated_image * 127.5 + 127.5).astype(np.uint8)  # Denormalize to [0, 255]
        tf.keras.preprocessing.image.save_img(f"{output_dir}/generated_image_{i}.png", generated_image[0])
    print(f"Generated {num_images} images based on the input text: '{input_text}'")

def train_and_generate_images(vishwamai, epochs, batch_size, input_text, num_images=10, output_dir="generated_images"):
    # Train the model
    vishwamai.train(epochs, batch_size)

    # Generate images based on input text
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for i in range(num_images):
        generated_image = vishwamai.generate_image(input_text)
        generated_image = (generated_image * 127.5 + 127.5).astype(np.uint8)  # Denormalize to [0, 255]
        tf.keras.preprocessing.image.save_img(f"{output_dir}/generated_image_{i}.png", generated_image[0])
    print(f"Generated {num_images} images based on the input text: '{input_text}'")

def generate_image(vishwamai, input_text):
    # Generate image based on input text using NLP and GAN
    inputs = vishwamai.tokenizer(input_text, return_tensors="tf")
    outputs = vishwamai.nlp_model(inputs)
    noise = np.random.normal(0, 1, (1, 100))
    noise = noise + outputs.last_hidden_state.numpy().flatten()[:100]  # Incorporate NLP model outputs into noise
    generated_image = vishwamai.generator.predict(noise)
    generated_image = (generated_image * 127.5 + 127.5).astype(np.uint8)  # Denormalize to [0, 255]
    return generated_image
