using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace calculadora
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            panel1.Visible = false;
            panel2.Visible = false;

        }

        int cambio = 0;

        private void button1_Click(object sender, EventArgs e)
        {
            panel1.Visible = true;
            panel2.Visible = false;
            cambio = 1;

            txtRadio.Text = " ";
            btnCCalcular.Text = "circulo";

            label3.Text = "Radio";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            panel1.Visible = false;
            panel2.Visible = true;
            label2.Text = "base";
            label1.Text = "altura";
            label4.Visible = false;
            txtlado.Visible = false;
            btnRCalcular.Text = "rectangulo";
            txtBase.Text = "";
            txtAltura.Text = "";
            lblRArea.Text = "area";
            lblRPerimetro.Text = "perimetro";
            cambio = 3;

        }

        private void btnCCalcular_Click(object sender, EventArgs e)
        {
            try
            {
                if (cambio == 1)
                {
                    circulo oCirculo = new circulo();
                    oCirculo.Radio = Convert.ToDouble(txtRadio.Text.Trim());
                    lblCArea.Text = "Area: " + oCirculo.area().ToString();
                    lblCPerimetro.Text = "Perimetro: " + oCirculo.perimetro().ToString();
                }
                else
                {
                    Cuadrado oCuadrado = new Cuadrado();
                    oCuadrado.Lados = Convert.ToDouble(txtRadio.Text.Trim());
                    lblCArea.Text = "Area: " + oCuadrado.area().ToString();
                    lblCPerimetro.Text = "Perimetro: " + oCuadrado.perimetro().ToString();
                }
            }
            catch
            {
                MessageBox.Show("insertar valores numericos", "Error de datos", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtRadio.Text = ""; lblCArea.Text = "Area:"; lblCPerimetro.Text = "Perimetro";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            panel1.Visible = true;
            panel2.Visible = false;
            cambio = 2;

            txtRadio.Text = " ";
            btnCCalcular.Text = "cuadrado";

            label3.Text = "lados";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            panel1.Visible = false;
            panel2.Visible = true;
            label2.Text = "base";
            label1.Text = "altura";
            label4.Visible = true;
            txtlado.Visible = true;
            btnRCalcular.Text = "triangulo";
            txtBase.Text = "";
            txtAltura.Text = "";
            txtlado.Text = "";
            lblRArea.Text = "area";
            lblRPerimetro.Text = "perimetro";
            cambio = 4;

        }

        private void btnRCalcular_Click(object sender, EventArgs e)
        {
            try
            {
                if (cambio == 3)
                {
                    rectangulo oRectangulo = new rectangulo();
                    oRectangulo.altura = Convert.ToDouble(txtAltura.Text.Trim());
                    oRectangulo.@base = Convert.ToDouble(txtBase.Text.Trim());
                    lblRArea.Text = "area: " + oRectangulo.area().ToString();
                    lblRPerimetro.Text = "perimetro: " + oRectangulo.perimetro().ToString();
                }
                else
                {
                    triangulo oTriangulo = new triangulo();
                    oTriangulo.Altura = Convert.ToDouble(txtAltura.Text.Trim());
                    oTriangulo.lado = Convert.ToDouble(txtlado.Text.Trim());
                    oTriangulo.@base = Convert.ToDouble(txtlado.Text.Trim());
                    lblRArea.Text = "area: " + oTriangulo.area().ToString();
                    lblRPerimetro.Text = "perimetro: " + oTriangulo.perimetro().ToString();
                }
            }
            catch
            {
                MessageBox.Show("insertar valores numericos", "error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                lblRArea.Text = "area:";
                lblRPerimetro.Text = "perimetro:";
                txtlado.Text = "";
                txtAltura.Text = ""; 
                txtBase.Text = "";

            }
        }

    }
}
