import { Component } from '@angular/core';
import { RouterLink, Router } from '@angular/router';
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

  constructor(
    private authService: AuthService,
    private router: Router
  ) {
    this.usuario = this.authService.getUsuarioActual();
  }

  cerrarSesion(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }

  isAdminOrAlmacenero() {
  return ['ADMIN', 'ALMACENERO'].includes(this.usuario?.rol);
}

isAdminOrVendedor() {
  return ['ADMIN', 'VENDEDOR'].includes(this.usuario?.rol);
}

isInternalUser() {
  return ['ADMIN', 'ALMACENERO', 'VENDEDOR'].includes(this.usuario?.rol);
}
}