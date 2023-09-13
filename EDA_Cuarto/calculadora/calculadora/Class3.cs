using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculadora
{
    class Cuadrado : figura
    {
        double lados;
        public Cuadrado() { }

        public double Lados
        {
            get { return lados; }
            set { lados = value; }
        }

        public override double area()
        {
            return Lados * Lados;
        }

        public override double perimetro()
        {
            return 4 * Lados;
        }
    }
}
