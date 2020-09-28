import React, {useState, useEffect} from 'react';
import { ScrollView, View } from 'react-native';
import { List } from 'react-native-paper';

interface MenuItem{
    text: string,
    link: string, 
    icon: HTMLElement   
};

const userMenuOptions = [
    {
        text: 'Start Trip',
        link: './start_trip',
        icon: <List.Icon icon="folder" />   
    },
    {
        text: 'History',
        link: './history',
        icon: <List.Icon icon="folder" />  
    },
    {    
        text: 'Current Trip',
        link: './current_trip',
        icon: <List.Icon icon="folder" />
    }
    
],
driverMenuOptions = [
        {
            text: 'Requests',
            link: './driver_requests',
            icon: <div></div>, 
        },
        {
            text: 'History',
            link: './history',
            icon: <div></div>  
        },
        {
            text: 'Current Job',
            link: './current_job',
            icon: <div></div>        
        }     
],
adminMenuOptions: MenuItem[] = [];

interface MenuType {
    driverMenuOptions: MenuItem[],
    userMenuOptions: MenuItem[],
    adminMenuOptions: MenuItem[]
};

const MenuComponent: React.FC<MenuType> = ({ 
    driverMenuOptions, 
    userMenuOptions, 
    adminMenuOptions 
}) => {
    
    const [menuOptionsType, setMenuOptionsType] = useState<string>('user');
  
    useEffect(() => {
        /**
         * Temporary will default to 'user'
         * waiting on backend development to be created
        */
    const getMenuType = () => 'user';
    
    setMenuOptionsType(getMenuType());     
    }, [])

    return (
        <View>
            <List.Section>
                <List.Subheader>Main Menu</List.Subheader>
                { menuOptionsType === 'user' && userMenuOptions && (
                    userMenuOptions.map(options => {
                     return(
                         <List.Item title={options.text} left={() => options?.icon} />
                     )   
                    }) 
                ) }
            </List.Section>        
        </View>
    )
}

export {
    MenuComponent, 
    userMenuOptions,
    driverMenuOptions,
    adminMenuOptions
};