import unittest

from complex_evaluate.evaluate import evaluate_edoal_string


class ComplexEvaluateTestCase(unittest.TestCase):

    def test_identity(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
  <Alignment>
    <map>
      <Cell>
        <entity1>
          <Class rdf:about="http://tont#PublicTransport" />
        </entity1>
        <entity2>
          <Class>
            <or rdf:parseType="Collection">
              <Class rdf:about="http://onto#Bus" />
              <Class rdf:about="http://onto#Train" />
              <Class rdf:about="http://onto#Metro" />
            </or>
          </Class>
        </entity2>
      </Cell>
    </map>
    <map>
      <Cell>
        <entity1>
          <Class rdf:about="http://tont#Conductor" />
        </entity1>
        <entity2>
          <Class rdf:about="http://onto#Driver" />
        </entity2>
      </Cell>
    </map>
  </Alignment>
</rdf:RDF>'''
        e2 = e1
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertEqual(f, 1.0)

    def test_order_invariance(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertEqual(f, 1.0)


    def test_error_penalization(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertLess(f, 1.0)

    def test_incompletness_penalization(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertLess(f, 1.0)

    def test_sensitivity1(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <and rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </and>
              </Class>
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertLess(f, 1.0)

    def test_sensitivity2(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Traine" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertLess(f, 1.0)

    def test_unordered_tree_sim(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Metro" />
                    <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#Conductor" />
            </entity1>
            <entity2>
              <Class rdf:about="http://onto#Driver" />
            </entity2>
          </Cell>
        </map>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                  <Class rdf:about="http://onto#Metro" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertEqual(f, 1.0)

    def test_edit_over_insert(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Metro" />
                    <Class rdf:about="http://onto#Bus" />
                  <Class rdf:about="http://onto#Train" />
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>

        <map>
          <Cell>
            <entity1>
              <Class rdf:about="http://tont#PublicTransport" />
            </entity1>
            <entity2>
              <Class>
                <or rdf:parseType="Collection">
                  <Class rdf:about="http://onto#Bus" />
                  <and rdf:parseType="Collection">
                      <Class rdf:about="http://onto#Train" />
                      <Class rdf:about="http://onto#Metro" />
                  </and>
                </or>
              </Class>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e3 = '''<?xml version="1.0" encoding="UTF-8"?>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
          <Alignment>
            <map>
              <Cell>
                <entity1>
                  <Class rdf:about="http://tont#PublicTransport" />
                </entity1>
                <entity2>
                  <Class>
                    <or rdf:parseType="Collection">
                      <Class rdf:about="http://onto#Bus" />
                      <or rdf:parseType="Collection">                          
                          <Class rdf:about="http://onto#Metro" />
                          <Class rdf:about="http://onto#Train" />
                      </or>
                    </or>
                  </Class>
                </entity2>
              </Cell>
            </map>
          </Alignment>
        </rdf:RDF>'''
        _, _, f1 = evaluate_edoal_string(e1, e3)
        _, _, f2 = evaluate_edoal_string(e2, e3)
        self.assertLess(f1, f2)


    def test_empty(self):
        e1 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
        <map>
          <Cell>
            <entity1>
            </entity1>
            <entity2>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        e2 = '''<?xml version="1.0" encoding="UTF-8"?>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:alext="http://exmo.inrialpes.fr/align/ext/1.0/" xmlns:align="http://knowledgeweb.semanticweb.org/heterogeneity/alignment#" xmlns:edoal="http://ns.inria.org/edoal/1.0/#" xmlns:xsd="http://www.w3.org/2001/XMLSchema#">
      <Alignment>
      <map>
          <Cell>
            <entity1>
            </entity1>
            <entity2>
            </entity2>
          </Cell>
        </map>
      </Alignment>
    </rdf:RDF>'''
        _, _, f = evaluate_edoal_string(e1, e2)
        self.assertEqual(f, 1.0)

if __name__ == '__main__':
    unittest.main()
