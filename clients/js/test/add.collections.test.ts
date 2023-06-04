 Here is the updated code:

import { expect, test } from '@jest/globals';
import chroma from './initClient'
import { DOCUMENTS, EMBEDDINGS, IDS } from './data';
import { METADATAS } from './data';
import { IncludeEnum } from "../src/types";

test("it should add single embeddings to a collection", async () => {
  await chroma.reset();
  const collection = await chroma.createCollection({ name: "test" });
  const ids = "test1";
  const embeddings = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const metadatas = { test: "test" };
  await collection.add({ ids, embeddings, metadatas });
  const count = await collection.count();
  expect(count).toBe(1);
  var res = await collection.get({
    ids: [ids], include: [
      IncludeEnum.Embeddings,
    ]
  });
  expect(res.embeddings![0]).toEqual(embeddings);
});

test("it should add batch embeddings to a collection", async () => {
 