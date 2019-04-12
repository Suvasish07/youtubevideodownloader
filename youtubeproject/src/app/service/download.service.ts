import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  constructor(private httpClient: HttpClient) { }
 
  searchVideosService(videourl){
    console.log(videourl);
    return this.httpClient.post('http://localhost:5001/videourl',{'videourl':videourl});
  }


}

