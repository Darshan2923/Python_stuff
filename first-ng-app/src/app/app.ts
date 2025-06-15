import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
// import { Home } from './home/home';
import { Header } from './components/header/header';

@Component({
  selector: 'app-root',
  // imports: [RouterOutlet, Home, Header],
  imports: [RouterOutlet, Header],
  template: `
    <!-- <h1>Welcome to {{ title }}!</h1>
    <p>Hello</p> -->
    <app-header> </app-header>
    <main>
      <router-outlet />
      <!-- <app-home></app-home> -->
    </main>
  `,
  styles: [
    `
      // p {
      //   background-color: red;
      // }

      main {
        padding: 16px;
      }
    `,
  ],
})
export class App {
  protected title = 'first-ng-app';
}
