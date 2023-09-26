import axios from 'axios';

export const getArticles = async () => {
	return axios
		.get('/api/articles')
		.then(function (response) {
			return response.data;
		})
		.catch(function (error) {
			throw error;
		});
};