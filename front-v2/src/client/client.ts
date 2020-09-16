import axios from "axios";
import { Response, Request } from "./types";

const baseURL = process.env.API_URL;

const httpClient = axios.create({
  baseURL,
  data: {}, // 空でも入れないとカスタムヘッダが付与されない
});

export const client = {
  sample: () => httpClient.get<Response.Sample>("/"),
  registerUser: (params: Request.RegisterUser) =>
    httpClient.post<Response.RegisterUser>("/register_user", params),
  getSynonyms: (params: Request.Search) =>
    httpClient.get<Response.Search>("/search", { params }),
  getAdjectiveTopics: (params: Request.ShowAdjectiveTopics) =>
    httpClient.post<Response.ShowAdjectiveTopics>("/show_adjective_topics", {
      ...params,
      noun: [],
      adjective: [],
    }),
  getNounTopics: (params: Request.ShowNounTopics) =>
    httpClient.post<Response.ShowNounTopics>("/show_noun_topics", params),
  getBooks: (params: Request.GetBooks) =>
    httpClient.post("/get_info_from_book_ids", params),
  registerBookIds: (params: Request.RegisterBookIds) =>
    httpClient.post("/register_book_ids", params),
  getEvaluationItems: () =>
    httpClient.get<Response.EvaluationItems>("/get_evaluation_data"),
  saveEvaluationData: (params: Request.SaveEvaluationData) =>
    httpClient.post("/save_evaluation_data", params),
};
