from datasets import load_dataset

def download_diffusiondb_subset(subset_name="large_random_1k", output_dir="diffusiondb_subset"):
    try:
        # Load the specified subset of the DiffusionDB dataset
        dataset = load_dataset('poloclub/diffusiondb', subset_name)

        # Save the dataset to the specified output directory
        dataset.save_to_disk(output_dir)

        print(f"Successfully downloaded and saved the {subset_name} subset to {output_dir}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    subset_name = "large_random_1k"  # Specify the subset to download
    output_dir = "diffusiondb_subset"  # Specify the output directory
    download_diffusiondb_subset(subset_name, output_dir)
