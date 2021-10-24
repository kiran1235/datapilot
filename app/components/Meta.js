import Head from 'next/head'
import { CNavbar, CNavbarBrand, CContainer  } from '@coreui/react'
const Meta = ({title, keywords, description}) => {
    return (
        <Head>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <meta charSet='utf-8' />
            <meta name='Keywords' content={keywords} />
            <meta name='description' content={description} />
            <link rel='icon' href='/favicon.ico' />
            <title>{title}</title>
        </Head>
    )
}

Meta.defaultProps = {
    title: 'DataPilot',
    keywords: 'DataPilot, database, management, system, dbms',
    description: 'database management system'
}
export default Meta