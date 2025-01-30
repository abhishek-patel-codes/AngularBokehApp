import { Injectable } from '@angular/core';
import{ HttpClient } from '@angular/common/http';





@Injectable({
  providedIn: 'root'
})
export class AddService {
  status:string="success"
  
  constructor(private http: HttpClient) { }
  addurl:string="http://127.0.0.1:5000/add"; //adding sample comment
  
  addData(FirstName,LastName,Email,gender,plan){
    this.http.post<any>(this.addurl,{"firstName":FirstName, "lastName":LastName,"email":Email,"gender":gender,"plan":plan}).subscribe(data => {
      this.status = data['status']
      if(this.status=="failure"){
        alert("Email already registered");
      };
    });
   
      
  }
}
