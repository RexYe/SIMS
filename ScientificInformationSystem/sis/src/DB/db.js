import DBF from './dbFactory'

export default DBF.context;

let prefix = 'http://localhost:8000'

DBF.create('Search',{
    get_authors_by_name:{
        url         :prefix+'/api/get_authors_by_name',
        method      :'GET',
    },
    get_personalinfo_by_uniid:{
        url         :prefix+'/api/get_personalinfo_by_uniid',
        method      :'GET',
    }
    // ,
    // account_register:{
    //     url         :prefix+'/api/account_register',
    //     method      :'POST',
    // },
})