export interface PedidoDetalle {
  productoId: number;
  nombre?: string;
  productoNombre?: string;
  cantidad: number;
  precio: number;
  subtotal: number;
}