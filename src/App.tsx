import React, { useState } from 'react';
import { ChakraProvider, Box, Heading, Text, Button, Input, VStack } from '@chakra-ui/react';
import './App.css';

function App() {
  const [description, setDescription] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const handleGenerate = async () => {
    try {
      const response = await fetch('http://10.240.176.61:5000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description }),
      });

      const data = await response.json();
      setImageUrl(`http://10.240.176.61:5000${data.image_url}`);
      console.log('Generated Image URL:', `http://10.240.176.61:5000${data.image_url}`); // Log the image URL to the console
    } catch (error) {
      console.error('Error generating image:', error);
    }
  };

  return (
    <ChakraProvider>
      <Box className="App">
        <Box as="header" bg="teal.500" color="white" p={4}>
          <Heading as="h1" size="lg">Image Generating Web App</Heading>
        </Box>
        <Box as="main" p={4}>
          <VStack spacing={4}>
            <Heading as="h2" size="md">Generate an Image</Heading>
            <Input
              placeholder="Describe the image you want to generate"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
            <Button colorScheme="teal" onClick={handleGenerate}>Generate</Button>
          </VStack>
          <Box mt={8}>
            <Heading as="h2" size="md">Generated Image</Heading>
            <Box border="1px" borderColor="gray.200" p={4} mt={4}>
              {imageUrl ? <img src={imageUrl} alt="Generated" /> : <Text>No image generated yet.</Text>}
            </Box>
          </Box>
        </Box>
        <Box as="footer" bg="teal.500" color="white" p={4} mt={8}>
          <Text>&copy; 2024 Image Generating Web App</Text>
        </Box>
      </Box>
    </ChakraProvider>
  );
}

export default App;
