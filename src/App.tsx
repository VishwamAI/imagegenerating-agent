import React from 'react';
import { ChakraProvider, Box, Heading, Text, Button, Input, VStack } from '@chakra-ui/react';
import './App.css';

function App() {
  return (
    <ChakraProvider>
      <Box className="App">
        <Box as="header" bg="teal.500" color="white" p={4}>
          <Heading as="h1" size="lg">Image Generating Web App</Heading>
        </Box>
        <Box as="main" p={4}>
          <VStack spacing={4}>
            <Heading as="h2" size="md">Generate an Image</Heading>
            <Input placeholder="Describe the image you want to generate" />
            <Button colorScheme="teal">Generate</Button>
          </VStack>
          <Box mt={8}>
            <Heading as="h2" size="md">Generated Image</Heading>
            <Box border="1px" borderColor="gray.200" p={4} mt={4}>
              <Text>No image generated yet.</Text>
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
