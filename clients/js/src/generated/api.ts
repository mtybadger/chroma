 Here are some examples of using the API:

```ts
import { ApiApi, ApiApiFactory } from './api';

// Create API instance
const api = ApiApiFactory();

// Add an embedding
const addResponse = await api.add('collectionId', {
  id: 'embeddingId',
  embedding: [0.1, 0.2, 0.3] 
});

// Get an embedding
const getResponse = await api.aGet('collectionId', { id: 'embeddingId' });

// Update an embedding
await api.update('collectionId', {
  id: 'embeddingId',
  embedding: [0.4, 0.5, 0.6] 
});

// Delete an embedding
await api.aDelete('collectionId', { id: 'embeddingId' });

// Count embeddings in a collection
const countResponse = await api.count('collectionId');

// Create a collection
await api.createCollection({ name: 'myCollection' });

// Get a collection
const collectionResponse = await api.getCollection('myCollection');

// Query for nearest neighbors
const neighborsResponse = await api