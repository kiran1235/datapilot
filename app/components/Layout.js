import styles from '../styles/Layout.module.css'
import Meta from './Meta'
import { CContainer, CRow, CCol, CSidebar, CSidebarBrand, CSidebarNav,CSidebarToggler, CNavbar, CNavbarBrand, CNavItem, CNavTitle,CBadge,CNavGroup } from '@coreui/react'
//import { CIcon } from '@coreui/icons-react'
//import * as icon from '@coreui/icons'

const Layout = ({children}) => {
    return (
        <>
            <Meta /> 
            <CNavbar colorScheme="light" className="bg-light" placement="fixed-top">
                <CContainer fluid>
                    <CNavbarBrand href="#">Fixed top</CNavbarBrand>
                </CContainer>
            </CNavbar>
            <div style={{marginTop: '4em', marginLeft: '1em'}}>
            <CRow className="justify-content-start">
                <CCol xs={2}>
                    <CSidebar>
                    <CSidebarBrand>Sidebar Brand</CSidebarBrand>
                    <CSidebarNav>
                        <CNavTitle>Nav Title</CNavTitle>
                        <CNavItem href="#">
                        
                        Nav item
                        </CNavItem>
                        <CNavItem href="#">
                        
                        With badge
                        <CBadge color="primary ms-auto">NEW</CBadge>
                        </CNavItem>
                        <CNavGroup toggler="Nav dropdown">
                        <CNavItem href="#">
                                Nav dropdown item
                        </CNavItem>
                        <CNavItem href="#">
                                Nav dropdown item
                        </CNavItem>
                        </CNavGroup>
                    </CSidebarNav>
                    <CSidebarToggler />
                    </CSidebar>                    
                </CCol>
                <CCol xs={8}>
                    {children}
                </CCol>
            </CRow>
            </div>
        </>

    )
}

export default Layout