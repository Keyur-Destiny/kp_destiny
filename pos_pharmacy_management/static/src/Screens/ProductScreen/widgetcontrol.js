/** @odoo-module **/

import ProductsWidgetControlPanel from "point_of_sale.ProductsWidgetControlPanel";
import Registries from "point_of_sale.Registries";
import {format} from "web.field_utils";
import utils from "web.utils";
const ProductsWidgetControlPanelInherit = (ProductsWidgetControlPanel) =>
    class ProductsWidgetControlPanelInherit extends ProductsWidgetControlPanel {

    setup() {
            super.setup();
            this.env.pos.showProductList = false;
          }
      _onClickShowProductList(ev){
       if (!this.env.pos.showProductList){
       this.env.pos.showProductList = true;
       }
       else{
       this.env.pos.showProductList = false;
       }
      }
    };

Registries.Component.extend(ProductsWidgetControlPanel, ProductsWidgetControlPanelInherit);
