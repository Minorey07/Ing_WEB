export interface CompraDetalle {
  id: number;
  compraId: number;
  productoId: number;
  productoNombre?: string;
  cantidad: number;
  precio: number;
  subtotal: number;
}