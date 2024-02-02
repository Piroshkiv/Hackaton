import React, { createContext, useEffect } from 'react'
import WeatherPage from './pages/WeatherPage'
import './styles/App.css';
import weatherStore from './store/weatherStore';


const storeWeather = new weatherStore();

export const Context = createContext({
  storeWeather
})
export default function App() {
  useEffect(() =>{
    storeWeather.getStartingWeather()
  }, [])
  return (
   <Context.Provider value={{storeWeather}}>
     <WeatherPage/>
   </Context.Provider>
  )
}
