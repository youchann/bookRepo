/* eslint-disable */
export namespace Response {
  export interface Sample {};

  export interface SuggestKeywords {
    keywords: string[];
  }
  export interface RegisterUser {
    id: number;
  }

  export interface ShowNounTopics {
    // NOTE: [book_id: number, words: strng[]][]
    noun_topics: [number, string[]][];
  }

  export interface GetBooks {
    info_list: {
      id: number;
      name: string;
      image_url: string;
    }[];
  }

  export interface EvaluationItems {
    evaluation_list: {
      id: number;
      description: string;
    }[];
  }
}

export namespace Request {
  export interface ShowNounTopics {
    inputed_word: string;    
  }

  export interface GetBooks {
    book_ids: number[];
  }

  export interface RegisterBookIds {
    user_id: number;
    book_ids: number[];
  }

  export interface SaveEvaluationData {
    user_id: number;
    evaluation_data: {
      evaluation_id: number;
      evaluation: number;
    }[]
  }
}
