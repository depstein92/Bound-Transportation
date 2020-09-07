import React, {useState, useEffect} from 'react';
import { ScrollView } from 'react-native';
import { Menu  } from 'react-native-paper';


interface MenuType {
    driverMenuOptions: Array<object>,
    userMenuOptions: Array<object>,
    adminMenuOptions: Array<object>
};

const userMenuOptions: Array<object> = [
    {
        text: 'Start Trip',
        link: './start_trip',
        component: <div></div>    
    },
    {
        text: 'History',
        link: './history',
        compponent: <div></div>  
    },
    {    
        text: 'Current Trip',
        link: './current_trip',
        component: <div></div>
    },
    {
        text: 'Log Out'        
    }
],
driverMenuOptions :  Array<object> = [
        {
            text: 'Requests',
            link: './driver_requests',
            component: <div></div>    
        },
        {
            text: 'History',
            link: './history',
            component: <div></div>  
        },
        {
            text: 'Current Job',
            link: './current_job',
            component: <div></div>        
        }     
],
adminMenuOptions: Array<object> = [];


const [menuOptionsType, setMenuOptionsType] = useState<string>('user');

useEffect(() => {
    /**
     * Temporary will default to 'user'
     * waiting on backend development to be created
    */
  const getMenuType = () => {
      return 'user';
  }
  setMenuOptionsType(getMenuType());     
}, [])

const MenuComponent: React.FC<MenuType> = ({ 
    driverMenuOptions, 
    userMenuOptions, 
    adminMenuOptions 
}) => {
    return (
        <ScrollView>
          {driverMenuOptions && menuOptionsType === "driver" && (
              <div></div>
          )} 
          {userMenuOptions && menuOptionsType === "user" && (
              <div></div>
          )} 
          {adminMenuOptions && menuOptionsType === "admin" && (
              <div></div>
          )}  
        </ScrollView>
    )
}

export default {MenuComponent, userMenuOptions};