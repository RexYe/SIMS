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
    add_organization:{
        url         :prefix+'/api/add_organization',
        method      :'GET',
    },  
    add_journal:{
        url         :prefix+'/api/add_journal',
        method      :'GET',
    }, 
    get_authors_list:{
        url         :prefix+'/api/get_authors_list',
        method      :'GET',
    }, 
    delete_author_by_uniid:{
        url         :prefix+'/api/delete_author_by_uniid',
        method      :'GET',
    }, 
    // ,
    // account_register:{
    //     url         :prefix+'/api/account_register',
    //     method      :'POST',
    // },
})