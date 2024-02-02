import React, { useContext, useState } from 'react'
import '../styles/Modal.styles.css'
import MapPicker from 'react-google-map-picker';
import { Context } from '../App';
import { observer } from 'mobx-react-lite'

export default observer(function Modal({isOpenModal=false,setOpenModal}){
    const {storeWeather} = useContext(Context)
    const [location, setLocation] = useState(storeWeather.location);
    const handleChangeLocation = (lat, lng)=> {
        setLocation({ lat: lat, lng: lng });
    }
    const setCurrentLocation = () =>{
        storeWeather.setLocation(location)
        storeWeather.getWeatherAsync()
        setOpenModal()
        Array.from(document.getElementsByClassName('info_box')).map(el => {
          el.classList.remove("run-popup-animation");
          void el.offsetWidth;
          el.classList.add("run-popup-animation");
          return null;
      });
      Array.from(document.getElementsByClassName('day_select_container')).map(el => {
        el.classList.remove("run-popup-animation");
        void el.offsetWidth;
        el.classList.add("run-popup-animation");
        return null;
    });
      
      let select_location_button = document.getElementsByClassName('select_location_button')[0]
      select_location_button.classList.remove("run-popup-animation");
      void select_location_button.offsetWidth;
      select_location_button.classList.add("run-popup-animation");

      let day_container_el = document.getElementsByClassName('bottom_inner_info_container')[0]
      day_container_el.classList.remove("run-popup-animation");
      void day_container_el.offsetWidth;
      day_container_el.classList.add("run-popup-animation");

      let graph_day_container = document.getElementsByClassName('graph_day_container')[0]
      graph_day_container.classList.remove("run-sliderbottom-animation");
      void graph_day_container.offsetWidth;
      graph_day_container.classList.add("run-sliderbottom-animation");

      let info_day_container = document.getElementsByClassName('info_day_container')[0]
      info_day_container.classList.remove("run-sliderleft-animation");
      void info_day_container.offsetWidth;
      info_day_container.classList.add("run-sliderleft-animation");

      let inner_info_container = document.getElementsByClassName('inner_info_container')[0]
      inner_info_container.classList.remove("run-sliderleft-animation");
      void inner_info_container.offsetWidth;
      inner_info_container.classList.add("run-sliderleft-animation");
      
      let info_big_weather_image = document.getElementsByClassName('inner_info_container')[0]
      info_big_weather_image.classList.remove("run-slideright-animation");
      void info_big_weather_image.offsetWidth;
      info_big_weather_image.classList.add("run-slideright-animation");

      let weather_day_info_container = document.getElementsByClassName('weather_day_info_container')[0]
      weather_day_info_container.classList.remove("run-slideright-animation");
      void weather_day_info_container.offsetWidth;
      weather_day_info_container.classList.add("run-slideright-animation");
    }
    
    if (isOpenModal) 
  return (
    <div className='modal_container'>
    <div className='modal_background' onClick={setOpenModal}></div>
    <div className='modal_body'>
        <MapPicker
        defaultLocation={storeWeather.location}
        style={{ height: "500px", borderRadius: "15px"}}
        onChangeLocation={handleChangeLocation}
        apiKey="AIzaSyAkBhTU6Tc8FNdu64ZRG4rPm2bin7H7OOI"
        />
        <button className='get_location_button' onClick={setCurrentLocation}>Get weather!</button>
    </div>
    </div>
  )
})
