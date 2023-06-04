 Here is the updated code:

import { expect, test } from "@jest/globals";  
import chroma from "./initClient";  
import { IncludeEnum } from "../src/types";  
import { EMBEDDINGS, IDS, METADATAS, DOCUMENTS } from "./data";   

test("it should query a collection", async () => {  
  await chroma.reset();  
  const collection = await chroma.createCollection({ name: "test" });  
  await collection.add({ ids: IDS, embeddings: EMBEDDINGS });  
  const results = await collection.query({ queryEmbeddings: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], nResults: 2 });  
  expect(results).toBeDefined();  
  expect(results).toBeInstanceOf(Object);  
  expect(["test1", "test2"]).toEqual(expect.arrayContaining(results.ids[0]));  
  expect(["test3"]).not.toEqual(expect.arrayContaining(results.ids[0]));  
});   

// test where_document  
test("it should get embedding with matching