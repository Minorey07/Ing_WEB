import { Routes } from '@angular/router';

import { Login } from './features/auth/login/login';
import { DashboardHome } from './features/dashboard/dashboard-home/dashboard-home';

import { ProductoComponent } from './features/producto-component/producto-component';
import { ClienteComponent } from './features/cliente-component/cliente-component';
import { ProveedorComponent } from './features/proveedor-component/proveedor-component';
import { CompraComponent } from './features/compra-component/compra-component';
import { PedidoComponent } from './features/pedido-component/pedido-component';
import { UsuarioComponent } from './features/usuario-component/usuario-component';
import { VentaComponent } from './features/venta-component/venta-component';

import { authGuard } from './guards/auth.guard';
import { roleGuard } from './guards/role.guard';

export const routes: Routes = [

  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },

  {
    path: 'login',
    component: Login
  },

  {
    path: 'dashboard',
    component: DashboardHome,
    canActivate: [authGuard]
  },

  {
    path: 'productos',
    component: ProductoComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'ALMACENERO'])
    ]
  },

  {
    path: 'clientes',
    component: ClienteComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'VENDEDOR'])
    ]
  },

  {
    path: 'proveedores',
    component: ProveedorComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'ALMACENERO'])
    ]
  },

  {
    path: 'compras',
    component: CompraComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'ALMACENERO'])
    ]
  },

  {
    path: 'pedidos',
    component: PedidoComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'ALMACENERO', 'VENDEDOR'])
    ]
  },

  {
    path: 'usuarios',
    component: UsuarioComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN'])
    ]
  },

  {
    path: 'ventas',
    component: VentaComponent,
    canActivate: [
      authGuard,
      roleGuard(['ADMIN', 'VENDEDOR'])
    ]
  },

  {
    path: '**',
    redirectTo: 'login'
  }

];