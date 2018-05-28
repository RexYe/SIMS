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
    },
    get_paper_title_by_uniid:{
        url         :prefix+'/api/get_paper_title_by_uniid',
        method      :'GET',
    },
    get_paper_detail_by_title:{
        url         :prefix+'/api/get_paper_detail_by_title',
        method      :'GET',
    },
    get_interpersonal_relationship_network_by_uniid:{
        url         :prefix+'/api/get_interpersonal_relationship_network_by_uniid',
        method      :'GET',
    },
    get_journal_by_name:{
        url         :prefix+'/api/get_journal_by_name',
        method      :'GET',
    },
    get_paper_by_journal_name:{
        url         :prefix+'/api/get_paper_by_journal_name',
        method      :'GET',
    },    
    get_journal_publish_every_year_by_journal_name:{
        url         :prefix+'/api/get_journal_publish_every_year_by_journal_name',
        method      :'GET',
    },
    get_journal_author_rank_by_journal_name:{
        url         :prefix+'/api/get_journal_author_rank_by_journal_name',
        method      :'GET',
    },
    get_journal_keyword_by_journal_name:{
        url         :prefix+'/api/get_journal_keyword_by_journal_name',
        method      :'GET',
    },
    get_organization_by_name:{
        url         :prefix+'/api/get_organization_by_name',
        method      :'GET',
    },
    get_paper_by_organization_name:{
        url         :prefix+'/api/get_paper_by_organization_name',
        method      :'GET',
    },
    get_organization_keyword_by_organization_name:{
        url         :prefix+'/api/get_organization_keyword_by_organization_name',
        method      :'GET',
    },
    get_organization_author_rank_by_organization_name:{
        url         :prefix+'/api/get_organization_author_rank_by_organization_name',
        method      :'GET',
    },
    get_organization_publish_every_year_by_organization_name:{
        url         :prefix+'/api/get_organization_publish_every_year_by_organization_name',
        method      :'GET',
    },
    get_organization_core_author_net_by_organization_name:{
        url         :prefix+'/api/get_organization_core_author_net_by_organization_name',
        method      :'GET',
    },
    // ,
    // account_register:{
    //     url         :prefix+'/api/account_register',
    //     method      :'POST',
    // },
})