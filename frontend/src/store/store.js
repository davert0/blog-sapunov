import { configureStore } from '@reduxjs/toolkit';
import { articleReducer } from './slices/article';


export const store = configureStore({
	reducer: {
		article: articleReducer,
	},
});

