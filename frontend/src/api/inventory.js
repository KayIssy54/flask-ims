import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";

export const getInventory = () =>
  axios.get(`${BASE_URL}/inventory`);

export const addItem = (data) =>
  axios.post(`${BASE_URL}/inventory`, data);

export const updateItem = (id, data) =>
  axios.patch(`${BASE_URL}/inventory/${id}`, data);

export const deleteItem = (id) =>
  axios.delete(`${BASE_URL}/inventory/${id}`);

export const getProduct = (barcode) =>
  axios.get(`${BASE_URL}/product/${barcode}`);