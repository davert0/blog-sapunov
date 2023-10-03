import { configureStore } from '@reduxjs/toolkit';
import { articleReducer } from './slices/article';
import { sessionReducer } from './slices/session';


export const store = configureStore({
	reducer: {
		article: articleReducer,
		session: sessionReducer,
	},
});

