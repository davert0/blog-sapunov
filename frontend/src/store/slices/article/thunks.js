import { createAsyncThunk } from '@reduxjs/toolkit';
import { actions } from './article';
import * as api from './api';

export const getArticles = createAsyncThunk(
	`/api/articles`,
	async (_, { dispatch }) => {
		try {
			const data = await api.getArticles();
			dispatch(actions.setArticles(data));
		} catch (e) {
			console.log(`${e}`);
		}
	},
);