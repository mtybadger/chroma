 Here is the updated code:

import {
    IncludeEnum,
    Metadata,
    Metadatas,
    Embedding,
    Embeddings,
    Document,
    Documents,
    Where,
    WhereDocument,
    ID,
    IDs,
    PositiveInteger,
    GetResponse,
    QueryResponse,
    AddResponse,
    CollectionMetadata
} from "./types";
import { IEmbeddingFunction } from './embeddings/IEmbeddingFunction';
import { ApiApi as DefaultApi } from "./generated";
import { handleError, handleSuccess } from "./utils";
import { toArray, toArrayOfArrays } from "./utils";


export class Collection {
    public name: string;
    public id: string;
    public metadata: CollectionMetadata | undefined;
    /**
     * @ignore
     */
    private api: DefaultApi;
    /**
     * @ignore
     */
    public embeddingFunction: IEmbeddingFunction | undefined;

    /**
     * @ignore
     */
    constructor(
        name: string,
        id: string,
        api: DefaultApi,
        metadata?: CollectionMetadata,
        embeddingFunction?: IEmbeddingFunction
    ) {
        this.name = name;
        this.id = id;
        this.metadata = metadata;
       