import axios from 'axios'

const instance = axios.create({
    baseURL:'http://127.0.0.1:8000/',
    headers:{
     "Content-Type":"application/json"
    }
})
export default (instance)
/*instance.interceptors.request.use(
    (config) =>{
        const token = localStorage.getItem('access_token')
        if(token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => Promise.reject(error)
)
instance .interceptors.response.use(
    (response)=>{
     async(error) =>{
        const originalrequest = error.config
        if(error.response?.status===401 && !originalrequest._retry){
            originalrequest.retry= true
            try{
                const refreshToken = localStorage.getItem('refresh_token')
                if(refreshToken){
                    const response = await axios.post(`${baseURL}/refresh`,{
                        refresh:refreshToken
                    })
                    const {access} = response.data
                    localStorage.getItem('access_token',access )
                    originalrequest.headers.Authorization = ` Bearer ${access}`
                    return axios(originalrequest)
                }

            }catch(refresherror){
                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')
                window.location.href='/login'
                return Promise.reject(refresherror)

            }
        }
     }
      return Promise.reject(error)
    }
    
  
)*/
