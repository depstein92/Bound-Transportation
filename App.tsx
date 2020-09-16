import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, AppRegistry } from 'react-native';
import { Provider as PaperProvider } from 'react-native-paper';
import appName from './app.json';
import {
  MenuComponent, 
  userMenuOptions, 
  driverMenuOptions,
  adminMenuOptions
} from './components/Menu';

export default function App() {
  return (
    <PaperProvider>
      <View style={styles.container}>
        <MenuComponent 
          userMenuOptions={userMenuOptions}
          driverMenuOptions={driverMenuOptions}
          adminMenuOptions={adminMenuOptions}
           />
      </View>
    </PaperProvider>
    
  );
}

AppRegistry.registerComponent(JSON.stringify(appName), () => App);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
