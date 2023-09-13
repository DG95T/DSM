
namespace calculadora
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.panel1 = new System.Windows.Forms.Panel();
            this.lblCArea = new System.Windows.Forms.Label();
            this.btnCCalcular = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.lblCPerimetro = new System.Windows.Forms.Label();
            this.txtRadio = new System.Windows.Forms.TextBox();
            this.panel2 = new System.Windows.Forms.Panel();
            this.lblRPerimetro = new System.Windows.Forms.Label();
            this.lblRArea = new System.Windows.Forms.Label();
            this.btnRCalcular = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.txtlado = new System.Windows.Forms.TextBox();
            this.txtAltura = new System.Windows.Forms.TextBox();
            this.txtBase = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(107, 42);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "circulo";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(779, 42);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(110, 23);
            this.button2.TabIndex = 1;
            this.button2.Text = "rectangulo";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.lblCArea);
            this.panel1.Controls.Add(this.btnCCalcular);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.lblCPerimetro);
            this.panel1.Controls.Add(this.txtRadio);
            this.panel1.Location = new System.Drawing.Point(12, 130);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(316, 263);
            this.panel1.TabIndex = 2;
            // 
            // lblCArea
            // 
            this.lblCArea.AutoSize = true;
            this.lblCArea.Location = new System.Drawing.Point(41, 157);
            this.lblCArea.Name = "lblCArea";
            this.lblCArea.Size = new System.Drawing.Size(37, 17);
            this.lblCArea.TabIndex = 4;
            this.lblCArea.Text = "area";
            // 
            // btnCCalcular
            // 
            this.btnCCalcular.Location = new System.Drawing.Point(131, 213);
            this.btnCCalcular.Name = "btnCCalcular";
            this.btnCCalcular.Size = new System.Drawing.Size(110, 30);
            this.btnCCalcular.TabIndex = 3;
            this.btnCCalcular.Text = "circulo\r\n";
            this.btnCCalcular.UseVisualStyleBackColor = true;
            this.btnCCalcular.Click += new System.EventHandler(this.btnCCalcular_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(41, 41);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(40, 17);
            this.label3.TabIndex = 2;
            this.label3.Text = "radio";
            // 
            // lblCPerimetro
            // 
            this.lblCPerimetro.AutoSize = true;
            this.lblCPerimetro.Location = new System.Drawing.Point(41, 111);
            this.lblCPerimetro.Name = "lblCPerimetro";
            this.lblCPerimetro.Size = new System.Drawing.Size(68, 17);
            this.lblCPerimetro.TabIndex = 1;
            this.lblCPerimetro.Text = "perimetro";
            // 
            // txtRadio
            // 
            this.txtRadio.Location = new System.Drawing.Point(44, 78);
            this.txtRadio.Name = "txtRadio";
            this.txtRadio.Size = new System.Drawing.Size(214, 22);
            this.txtRadio.TabIndex = 0;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.lblRPerimetro);
            this.panel2.Controls.Add(this.lblRArea);
            this.panel2.Controls.Add(this.btnRCalcular);
            this.panel2.Controls.Add(this.label4);
            this.panel2.Controls.Add(this.label1);
            this.panel2.Controls.Add(this.txtlado);
            this.panel2.Controls.Add(this.txtAltura);
            this.panel2.Controls.Add(this.txtBase);
            this.panel2.Controls.Add(this.label2);
            this.panel2.Location = new System.Drawing.Point(439, 130);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(492, 263);
            this.panel2.TabIndex = 3;
            // 
            // lblRPerimetro
            // 
            this.lblRPerimetro.AutoSize = true;
            this.lblRPerimetro.Location = new System.Drawing.Point(81, 167);
            this.lblRPerimetro.Name = "lblRPerimetro";
            this.lblRPerimetro.Size = new System.Drawing.Size(68, 17);
            this.lblRPerimetro.TabIndex = 8;
            this.lblRPerimetro.Text = "perimetro";
            // 
            // lblRArea
            // 
            this.lblRArea.AutoSize = true;
            this.lblRArea.Location = new System.Drawing.Point(81, 122);
            this.lblRArea.Name = "lblRArea";
            this.lblRArea.Size = new System.Drawing.Size(37, 17);
            this.lblRArea.TabIndex = 7;
            this.lblRArea.Text = "area";
            // 
            // btnRCalcular
            // 
            this.btnRCalcular.Location = new System.Drawing.Point(213, 213);
            this.btnRCalcular.Name = "btnRCalcular";
            this.btnRCalcular.Size = new System.Drawing.Size(88, 30);
            this.btnRCalcular.TabIndex = 6;
            this.btnRCalcular.Text = "triangulo";
            this.btnRCalcular.UseVisualStyleBackColor = true;
            this.btnRCalcular.Click += new System.EventHandler(this.btnRCalcular_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(386, 41);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(35, 17);
            this.label4.TabIndex = 5;
            this.label4.Text = "lado";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(226, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(44, 17);
            this.label1.TabIndex = 4;
            this.label1.Text = "altura";
            // 
            // txtlado
            // 
            this.txtlado.Location = new System.Drawing.Point(350, 78);
            this.txtlado.Name = "txtlado";
            this.txtlado.Size = new System.Drawing.Size(100, 22);
            this.txtlado.TabIndex = 3;
            // 
            // txtAltura
            // 
            this.txtAltura.Location = new System.Drawing.Point(201, 78);
            this.txtAltura.Name = "txtAltura";
            this.txtAltura.Size = new System.Drawing.Size(100, 22);
            this.txtAltura.TabIndex = 2;
            // 
            // txtBase
            // 
            this.txtBase.Location = new System.Drawing.Point(55, 78);
            this.txtBase.Name = "txtBase";
            this.txtBase.Size = new System.Drawing.Size(100, 22);
            this.txtBase.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(81, 41);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(39, 17);
            this.label2.TabIndex = 0;
            this.label2.Text = "base";
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(319, 42);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(94, 23);
            this.button3.TabIndex = 4;
            this.button3.Text = "cuadrado";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(575, 42);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 5;
            this.button4.Text = "triangulo";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1014, 601);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Label lblCPerimetro;
        private System.Windows.Forms.TextBox txtRadio;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label lblCArea;
        private System.Windows.Forms.Button btnCCalcular;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtlado;
        private System.Windows.Forms.TextBox txtAltura;
        private System.Windows.Forms.TextBox txtBase;
        private System.Windows.Forms.Button btnRCalcular;
        private System.Windows.Forms.Label lblRPerimetro;
        private System.Windows.Forms.Label lblRArea;
    }
}

