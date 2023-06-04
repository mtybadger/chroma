 Here is the updated code:

import { expect, test } from "@jest/globals";
import chroma from "./initClient";
import { IncludeEnum } from "../src/types";
import { IDS, DOCUMENTS, EMBEDDINGS, METADATAS } from "./data";

test("it should get embedding with matching documents", async () => {
  await chroma.reset();
  const collection = await chroma.createCollection({ name: "test" });
  await collection.add({ ids: IDS, embeddings: EMBEDDINGS, metadatas: METADATAS, documents: DOCUMENTS });

  const results = await collection.get({
    ids: ["test1"],
    include: [
      IncludeEnum.Embeddings,
      IncludeEnum.Metadatas,
      IncludeEnum.Documents,
    ]
  });
  expect(results).toBeDefined();
  expect(results).toBeInstanceOf(Object);
  expect(results.embeddings![0]).toEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

  await collection.update({
    ids: ["test1"],
    embeddings: [[1,