// import { createAsyncThunk } from '@reduxjs/toolkit';
// import { message } from 'antd';

// import { actions } from './collection';
// import * as api from './api';
// import { IResponseCollectionData, IResponseCollectionItems } from './type';

// export const getCollections = createAsyncThunk(
// 	`api/get/collection/tree`,
// 	async (_, { dispatch }) => {
// 		try {
// 			const data = await api.getCollections();
// 			dispatch(actions.setData(data));
// 		} catch (e) {
// 			message.error(`${e}`);
// 		}
// 	},
// );

// export const getCollectionItems = createAsyncThunk(
// 	`api/get/collection/collectionId/items`,
// 	async (collectionId, { dispatch }) => {
// 		try {
// 			const data = await api.getCollectionItems(collectionId);
// 			dispatch(actions.setItems(data));
// 		} catch (e) {
// 			message.error(`${e}`);
// 		}
// 	},
// );
