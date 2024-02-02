import React, { useContext, useState } from 'react'
import { observer } from 'mobx-react-lite'
import Modal from '../components/Modal'
import { Context } from '../App'
import { Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faAngleRight, faCloudSun, faDroplet, faSnowflake, faSun, faTemperatureLow, faWind } from '@fortawesome/free-solid-svg-icons'
import '../styles/WeatherPage.styles.css'
import DaySelectSpinner from '../components/DaySelectSpinner'



export default observer(function WeatherPage() {
  const [openModal, setOpenModal] = useState(false)
  const {storeWeather} = useContext(Context)
  const getCurrentLocation = () => {
    setOpenModal(true)
  }

  const dateFormatter = (date)=> {
    const options = { year: 'numeric', month: 'short', day: 'numeric',weekday: 'long' };
    return new Date(date).toLocaleDateString("en-US", options)
  }

  return (
    <div className='page_container'>
      <Modal isOpenModal={openModal} setOpenModal={()=> setOpenModal(false)}/>
        <div className='top_info_container'>
            <div className='inner_info_container run-sliderleft-animation'>
                <div className='top_inner_info_container'>
                    <button className='select_location_button run-popup-animation' onClick={getCurrentLocation}>Set location <FontAwesomeIcon icon={faAngleRight}/></button>
                </div>
                <div className='bottom_inner_info_container run-popup-animation'>
                  <p className='big_standart_text'>{storeWeather.selectedDayWeather.avg_temperature}&#8451;</p>
                  <p className='small_standart_text'>{dateFormatter(storeWeather.selectedDayWeather.date).split(',')[0]} | {dateFormatter(storeWeather.selectedDayWeather.date).split(',').slice(1).join(',')}</p>
                </div>
            </div>
            <FontAwesomeIcon icon={faCloudSun} className='info_big_weather_image run-slideright-animation '/>
        </div>
        <div className='bottom_info_container'>
          <div className='all_info_container'>
            <div className='info_day_container run-sliderleft-animation '>
              <DaySelectSpinner/>
            </div>
            <div className='graph_day_container run-sliderbottom-animation'>
            <ResponsiveContainer width="95%" height="95%" className="graph_day_weather">
              <LineChart data={storeWeather.weatherDataSet.week_info} >
                <XAxis dataKey="date" />
                <YAxis/>
                <Tooltip wrapperClassName='graph_day_weather_tooltip' contentStyle={{background: "var(--color-background-container-additional-2-weatherApp)", border:"none"}}/>
                <Line type="monotone" dataKey="temperature" stroke="#4e3912" />
              </LineChart>
            </ResponsiveContainer>
            </div>
          </div>
          <div className='weather_day_info_container run-slideright-animation'>
            <div className='info_box run-popup-animation'>
              <FontAwesomeIcon icon={faTemperatureLow} className='image_info_box'/>
              <div className='text_info_box'>
              <p className='small_standart_text'>Avarage temperature</p>
              <p className='medium_standart_text'>{storeWeather.selectedDayWeather.avg_temperature}&#8451;</p>
              </div>
            </div>
            <div className='info_box run-popup-animation'>
              <FontAwesomeIcon icon={faWind} className='image_info_box'/>
              <div className='text_info_box'>
              <p className='small_standart_text'>Precipitation</p>
              <p className='medium_standart_text'>{storeWeather.selectedDayWeather.precipitation}</p>
              </div>
            </div>
            <div className='info_box run-popup-animation'>
              <FontAwesomeIcon icon={faDroplet} className='image_info_box'/>
              <div className='text_info_box'>
              <p className='small_standart_text'>Rain</p>
              <p className='medium_standart_text'>{storeWeather.selectedDayWeather.rain_sum}</p>
              </div>
            </div>
            <div className='info_box run-popup-animation'>
              <FontAwesomeIcon icon={faSnowflake} className='image_info_box'/>
              <div className='text_info_box'>
              <p className='small_standart_text'>Snow</p>
              <p className='medium_standart_text'>{storeWeather.selectedDayWeather.snowfall_sum}</p>
              </div>
            </div>
            <div className='info_box run-popup-animation'>
              <FontAwesomeIcon icon={faSun} className='image_info_box'/>
              <div className='text_info_box'>
              <p className='small_standart_text'>Shortwave radiation</p>
              <p className='medium_standart_text'>{storeWeather.selectedDayWeather.shortwave_radiation_sum}</p>
              </div>
              </div>
          </div>
        </div>
    </div>
  )
})
