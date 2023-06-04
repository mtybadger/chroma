 Here is the updated code:

import { expect, test, beforeEach } from "@jest/globals";
import chroma from "./initClient";

beforeEach(async () => {
  await chroma.reset();
});

test("it should list collections", async () => {
  let collections = await chroma.listCollections();
  expect(collections).toBeDefined();
  expect(collections).toBeInstanceOf(Array);
  expect(collections.length).toBe(0);
  const collection = await chroma.createCollection({ name: "test" });
  collections = await chroma.listCollections();
  expect(collections.length).toBe(1);
});

test("it should create a collection", async () => {
  const collection = await chroma.createCollection({ name: "test" });
  expect(collection).toBeDefined();
  expect(collection).toHaveProperty("name");
  expect(collection).toHaveProperty('id')
  expect(collection.name).toBe("test");
  let collections = await chroma.listCollections();
  expect([{ name: "test", metadata: null, id: collection.id }]).toEqual