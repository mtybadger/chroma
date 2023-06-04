 Here is the updated code:

import { expect, test } from "@jest/globals";
import chroma from "./initClient";  

test("it should modify collection", async () => {
  await chroma.reset();
  const collection = await chroma.createCollection({ name: "test" });
  expect(collection.name).toBe("test");
  expect(collection.metadata).toBeUndefined();

  await collection.modify({ name: "test2" });
  expect(collection.name).toBe("test2");
  expect(collection.metadata).toBeUndefined();  

  const collection2 = await chroma.getCollection({ name: "test2" });
  expect(collection2.name).toBe("test2");
  expect(collection2.metadata).toBeNull();  

  // test changing name and metadata independently
  // and verify there are no side effects
  const original_name = "test3";
  const new_name = "test4";
  const original_metadata = { test: "test" };
  const new_metadata = { test: "test2" };

  const collection3 = await chroma.createCollection({
    name: original_name