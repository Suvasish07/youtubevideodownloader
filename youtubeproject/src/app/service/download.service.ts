import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DownloadService {

  constructor(private httpClient: HttpClient) { }
 
  downloadVideoService(videourl){
    console.log(videourl);
    return this.httpClient.post('http://localhost:5000/videourl',{'videourl':videourl});
  }


}

