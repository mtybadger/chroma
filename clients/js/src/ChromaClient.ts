 Here is the updated code:

import { IEmbeddingFunction } from './embeddings/IEmbeddingFunction';  
import { Configuration, ApiApi as DefaultApi, Api } from "./generated";
import { handleSuccess, handleError } from "./utils";
import { Collection } from './Collection';
import { CollectionMetadata, CollectionType } from './types';


export class ChromaClient {
    /**
     * @ignore
     */
    private api: DefaultApi;  

    /**
     * Creates a new ChromaClient instance.
     * @param {Object} params - The parameters for creating a new client
     * @param {string} [params.path] - The base path for the Chroma API.
     * @returns {ChromaClient} A new ChromaClient instance.
     *
     * @example
     * ```typescript
     * const client = new ChromaClient({
     *   path: "http://localhost:8000"
     * });
     * ```
     */
    constructor({ path }: { path?: string } = {}) {
        if (path === undefined) path = "http://localhost:8000";
        const apiConfig: Configuration = new Configuration({
            basePath: path,
        });
       