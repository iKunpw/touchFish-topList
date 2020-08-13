import req from '../http'

export default class GETHOT {
    get_zhihu(data) {
        return req.post('/api/get_zhihu', data)
    }
    get_v2ex(data) {
        return req.post('/api/get_v2ex', data)
    }
    get_weibo(data) {
        return req.post('/api/get_weibo', data)
    }
    get_52pojie(data) {
        return req.post('/api/get_52pojie', data)
    }
}