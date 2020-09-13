/* eslint-disable */
export namespace Response {
  export interface Sample {};

  export interface RegisterUser {
    id: number;
    student_number: number;
  }

  export interface Search {
    analyzed_keywords: {
      adjective: string[];
      noun: string[];
    };
    similar_words: string[];
  }

  export interface ShowAdjectiveTopics {
    // NOTE: [book_id: number, words: strng[]][]
    adjective_topics: [number, string[]][];
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
  export interface RegisterUser {
    student_number: number;
  }

  export interface Search {
    keyword: string;
  }

  export interface ShowAdjectiveTopics {
    noun: string[];
    adjective: string[];
    selected_keywords: string[];
  }

  export interface ShowNounTopics {
    book_ids: number[];
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