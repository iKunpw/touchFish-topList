import axios from "axios";
// import router from "../router";
// import ElementUI, { Loading } from "element-ui";
// import store from "../store/index";
/* let u = process.env.API_HOST;
axios.defaults.baseURL = u; */

const urlDev = 'http://127.0.0.1:5000';

let urlOfWeb = window.location.host;


if (urlOfWeb == 'localhost:8080') {
    axios.defaults.baseURL = urlDev;
}
// else if (urlOfWeb == '') {
//     axios.defaults.baseURL = urlTest;
// }

/* axios.defaults.timeout = 1500; */
// axios.defaults.withCredentials = true;

// 添加请求拦截器
// axios.interceptors.request.use(
//     async config => {
//         let time = parseInt(new Date().getTime() / 1000);
//         if (config.url != "/api/AdminLogin") {
//             let token = sessionStorage.getItem("token");
//             let tokenTime = parseInt(sessionStorage.getItem("time"));
//             let retokenTime = parseInt(sessionStorage.getItem("re_time"));
//             let expire_time = parseInt(sessionStorage.getItem("expire_time"));
//             let expire_re_time = parseInt(sessionStorage.getItem("expire_re_time"));

//             let state1 = time - tokenTime > expire_time;
//             let state2 = time - retokenTime > expire_re_time;
//             if (state1) {
//                 if (state2) {
//                     router.push("/");
//                     sessionStorage.clear();
//                 } else {
//                     sessionStorage.setItem("time", parseInt(new Date().getTime() / 1000));
//                     sessionStorage.setItem(
//                         "re_time",
//                         parseInt(new Date().getTime() / 1000)
//                     );
//                     await axios({
//                         url: "/api/refreshToken",
//                         method: "post",
//                         data: {
//                             refresh_token: sessionStorage.getItem("refresh_token")
//                         }
//                     }).then(res => {
//                         if (res.data.err_code == 200) {
//                             sessionStorage.setItem("time", res.data.data.token_create_time);
//                             sessionStorage.setItem(
//                                 "re_time",
//                                 res.data.data.refresh_token_create_time
//                             );

//                             sessionStorage.setItem("expire_time", res.data.data.token_expire);
//                             sessionStorage.setItem(
//                                 "expire_re_time",
//                                 res.data.data.refresh_token_expire
//                             );

//                             sessionStorage.setItem(
//                                 "refresh_token1",
//                                 res.data.data.refresh_token
//                             );
//                             sessionStorage.setItem("token1", res.data.data.token);
//                         }
//                     });
//                 }
//                 config.headers["Authorization"] =
//                     "Bearer " + sessionStorage.getItem("token1");
//             } else {}
//             config.headers["Authorization"] =
//                 "Bearer " + sessionStorage.getItem("token");
//         } else {}
//         config.headers["Content-Type"] = "application/json";
//         return config;
//     },
//     error => {
//         return Promise.reject(error);
//     }
// );

// 添加响应拦截器
// axios.interceptors.response.use(
//     function(res) {
//         if (res.data.code == 507 || res.data.code == 508 || res.data.code == 402) {
//             ElementUI.Message({
//                 message: res.data.message[0],
//                 type: "error"
//             });
//             setTimeout(() => {
//                 router.push("/");
//             }, 1500);
//         }

//         return res;
//     },
//     function(error) {
//         return Promise.reject(error);
//     }
// );

export default axios;