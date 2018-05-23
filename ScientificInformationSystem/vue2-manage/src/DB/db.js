import DBF from './dbFactory'

export default DBF.context;

let prefix = 'http://localhost:8000'

DBF.create('Search',{
    user_login:{
        url         :prefix+'/api/user_login',
        method      :'GET',
    },
    add_authors:{
        url         :prefix+'/api/add_authors',
        method      :'GET',
    },	
    // ,
    // account_register:{
    //     url         :prefix+'/api/account_register',
    //     method      :'POST',
    // },
})