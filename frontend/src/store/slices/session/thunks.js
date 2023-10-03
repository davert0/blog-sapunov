import { createAsyncThunk } from '@reduxjs/toolkit';

import { actions } from './session';
import * as api from './api';

export const getToken = createAsyncThunk(
	`api/post/user/token`,
	async (values, { dispatch }) => {
		try {
			dispatch(actions.setIsLoading(true));
			const data = await api.getToken(values);
			localStorage.setItem('access_token', data.access_token);
			dispatch(actions.setToken(data));
			await dispatch(getUser());
		} catch (e) {
			console.log(`${e}`);
		} finally {
			dispatch(actions.setIsLoading(false));
		}
	},
);

export const getUser = createAsyncThunk(
	`api/get/user`,
	async (_, { dispatch }) => {
		try {
			dispatch(actions.setIsLoading(true));
			const data = await api.getUser();
			dispatch(actions.setUser(data));
		} catch (e) {
			console.log(`${e}`);
		} finally {
			dispatch(actions.setIsLoading(false));
		}
	},
);

