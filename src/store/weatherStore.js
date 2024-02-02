import {makeAutoObservable} from "mobx"
//import api from "../config/http";

export default class weatherStore {

    location = {}

    weatherDataSet = {}
    selectedDayWeather = {}
    constructor(){
        makeAutoObservable(this);
    }

    setLocation(object){
        this.location = object;
    }
    setInitialSelectedDayWeather(){
        this.selectedDayWeather = this.weatherDataSet.weather_data[0]
    }
    setSelectedDayWeather(date){     
        this.selectedDayWeather = this.weatherDataSet.weather_data.filter(data => data.date === date)[0];
    }
    
    setWeatherDataSet(object){
        this.weatherDataSet = object;
    }

    async getWeatherAsync(){
        const start_date = new Date().toISOString().split('T')[0]
        const end_date = new Date(new Date().setDate(new Date().getDate() + 7)).toISOString().split('T')[0]
        const payload =  { lat: this.location.lat, lng: this.location.lng, start_date, end_date}
        console.log(payload)
        try {
          // const {data} = await api.post(`post/`,payload)
        } catch (error) {
          console.log(error)
        }
        const data = {
            start_date: "2024-02-02",
            end_date: "2024-02-02",
            location:"Kiev",
            weather_data: [
              {
                date: "2024-02-02",
                avg_temperature: 22,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },
              {
                date: "2024-02-03",
                avg_temperature: 21,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },
              {
                date: "2024-02-04",
                avg_temperature: 25,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },{
                date: "2024-02-05",
                avg_temperature: 28,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },{
                date: "2024-02-06",
                avg_temperature: 21,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },{
                date: "2024-02-07",
                avg_temperature: 20,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              },{
                date: "2024-02-08",
                avg_temperature: 19,
                precipitation: 0,
                rain_sum: 0,
                snowfall_sum: 0,
                shortwave_radiation_sum: 0
              }
            ],
          }
        this.setWeatherDataSet(data)
        this.getWeekInfo()
        this.setInitialSelectedDayWeather()
    }

    getWeekInfo(){
        const week_info = this.weatherDataSet.weather_data.map(weatherData => {
            return {
                date:weatherData.date.split('-').slice(1).join('.'),
                temperature:weatherData.avg_temperature
            }
        })
        this.weatherDataSet.week_info = week_info
    }

    async getStartingWeather(){

        const payload =  { lat: 50.45, lng: 30.54}
        this.setLocation(payload)
        this.getWeatherAsync()
        this.getWeekInfo()
        this.setInitialSelectedDayWeather()
    }
}
