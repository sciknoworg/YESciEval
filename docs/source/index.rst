

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/YESciEval/main/images/logo.png" alt="OntoLearner Logo" width="500"/>
   </div>

.. raw:: html

   <div align="center">
     <a href="https://badge.fury.io/py/YESciEval"><img src="https://badge.fury.io/py/YESciEval.svg" alt="PyPI version"></a>
     <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
     <a href="https://yescieval.readthedocs.io/"><img src="https://app.readthedocs.org/projects/yescieval/badge/" alt="Documentation Status"></a>

   </div>

   <br>
   <br>

YESciEval provides a comprehensive library for evaluating the quality of synthesized scientific answers using predefined rubrics and sophisticated LLM-based judgment models. This framework enables you to assess answers on key criteria by utilizing pretrained judges and parsing LLM outputs into structured JSON formats for detailed analysis.

YESciEval was created by `Scientific Knowledge Organization (SciKnowOrg group) <https://github.com/sciknoworg/>`_ at `Technische Informationsbibliothek (TIB) <https://www.tib.eu/de/>`_. Don't hesitate to open an issue on the `YESciEval repository <https://github.com/sciknoworg/YESciEval>`_ if something is broken or if you have further questions.

.. seealso::

   See the `Quickstart <quickstart.html>`_ for more quick information on how to use OntoLearner.



If you find this repository helpful, feel free to cite our publication `YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering  <https://arxiv.org/abs/2505.14279>`_:

 .. code-block:: bibtex

    @article{d2025yescieval,
      title={YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering},
      author={D'Souza, Jennifer and Giglou, Hamed Babaei and M{\"u}nch, Quentin},
      journal={arXiv preprint arXiv:2505.14279},
      year={2025}
    }



.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   installation
   quickstart

.. toctree::
   :maxdepth: 1
   :caption: Evaluator
   :hidden:

   rubrics
   judges

.. toctree::
   :maxdepth: 1
   :caption: Package Reference
   :glob:
   :hidden:

   package_reference/base
   package_reference/judge
   package_reference/rubric
   package_reference/
