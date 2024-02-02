import React, { useContext, useEffect, useState } from 'react'
import '../styles/DaySelectSpinner.styles.css'
import { Context } from '../App'
import { faCloud } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
export default function DaySelectSpinner() {

    const {storeWeather} = useContext(Context)
    const [dateArray, setDateArray] = useState([])
    const setCurrentWeather = (date, key)=> {
        storeWeather.setSelectedDayWeather(date)
        Array.from(document.getElementsByClassName('info_box')).map(el => {
            el.classList.remove("run-popup-animation");
            void el.offsetWidth;
            el.classList.add("run-popup-animation");
            return null;
        });
        Array.from(document.getElementsByClassName('day_select_container')).map(el => {
            if(Number(el.getAttribute('set_key')) === key) el.classList.add('day_container_selected')
            else  el.classList.remove('day_container_selected')
            return null;
        });
        let el = document.getElementsByClassName('bottom_inner_info_container')[0]
        el.classList.remove("run-popup-animation");
        void el.offsetWidth;
        el.classList.add("run-popup-animation");
    }
    useEffect(()=>{
        let tempDateArray = []
        for(let i=0; i<7;i++){
            tempDateArray.push(new Date(new Date().setDate(new Date().getDate() + i)).toISOString().split('T')[0])
        }
        setDateArray(dateArray => dateArray = [...tempDateArray])
    },[setDateArray])
  return (
    <div className='spinner_container'>
        {dateArray.map((date, i) =>
        <div className='day_select_container run-popup-animation' key={i} set_key={i}>
            <FontAwesomeIcon icon={faCloud} className='day_select_image'/>
            <button className="day_select_button" onClick={()=> setCurrentWeather(date, i)}>{date.split('-').slice(1).join('.')}</button>
        </div>
        )}
    </div>
  )
}
