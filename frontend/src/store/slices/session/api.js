import axios from "axios";


export const getToken = async (values) => {
  return axios
    .post("api/user/token", values)
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      throw error;
    });
};

export const getUser = async () => {
	const config = {
		headers: {
		  Authorization: `Bearer ${localStorage.getItem("access_token")}`,
		},
	  };
	  
  return axios
    .get("api/user/me", config)
    .then(function (response) {
      return response.data;
    })
    .catch(function (error) {
      throw error;
    });
};
