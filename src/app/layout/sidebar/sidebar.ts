import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  templateUrl: './sidebar.html',
  styleUrls: ['./sidebar.css'],
  imports: [
    RouterLink,
    CommonModule
  ]
})
export class Sidebar {

  usuario: any;

  constructor(private authService: AuthService) {
    this.usuario = this.authService.getUsuarioActual();
  }
}